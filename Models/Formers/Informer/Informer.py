
import torch
import torch.nn as nn
import torch.nn.functional as F
from Models.Formers.Layers.Transformer_EncDec import Decoder, DecoderLayer, Encoder, EncoderLayer, ConvLayer
from Models.Formers.Layers.SelfAttention_Family import FullAttention, ProbAttention, AttentionLayer
from Models.Formers.Embed import DataEmbedding_wo_pos_temp,DataEmbedding_wo_temp,FixedEmbedding
import numpy as np


class Model(nn.Module):
    """
    Informer with Propspare attention in O(LlogL) complexity
    """
    def __init__(self, configs):
        super(Model, self).__init__()
        self.pred_len = configs.forecast_horizon
        self.output_attention = configs.output_attention

        if configs.embed_type == 0:
            self.enc_embedding = DataEmbedding_wo_temp(configs.num_series, configs.d_model, configs.embed, configs.freq, configs.dropout)
            self.dec_embedding = DataEmbedding_wo_temp(configs.num_series, configs.d_model, configs.embed, configs.freq, configs.dropout)

        elif configs.embed_type == 1:
            self.enc_embedding = DataEmbedding_wo_pos_temp(configs.num_series, configs.d_model, configs.embed, configs.freq,
                                                           configs.dropout)
            self.dec_embedding = DataEmbedding_wo_pos_temp(configs.num_series, configs.d_model, configs.embed, configs.freq,
                                                           configs.dropout)
        # Encoder
        self.encoder = Encoder(
            [
                EncoderLayer(
                    AttentionLayer(
                        ProbAttention(False, configs.factor, attention_dropout=configs.dropout,
                                      output_attention=configs.output_attention),
                        configs.d_model, configs.n_heads),
                    configs.d_model,
                    configs.d_ff,
                    dropout=configs.dropout,
                    activation=configs.activation
                ) for l in range(configs.e_layers)
            ],
            [
                ConvLayer(
                    configs.d_model
                ) for l in range(configs.e_layers - 1)
            ] if configs.distil else None,
            norm_layer=torch.nn.LayerNorm(configs.d_model)
        )
        # Decoder
        self.decoder = Decoder(
            [
                DecoderLayer(
                    AttentionLayer(
                        ProbAttention(True, configs.factor, attention_dropout=configs.dropout, output_attention=False),
                        configs.d_model, configs.n_heads),
                    AttentionLayer(
                        ProbAttention(False, configs.factor, attention_dropout=configs.dropout, output_attention=False),
                        configs.d_model, configs.n_heads),
                    configs.d_model,
                    configs.d_ff,
                    dropout=configs.dropout,
                    activation=configs.activation,
                )
                for l in range(configs.d_layers)
            ],
            norm_layer=torch.nn.LayerNorm(configs.d_model),
            projection=nn.Linear(configs.d_model, configs.num_series, bias=True)
        )

    def forward(self, x_enc, x_dec, enc_self_mask=None, dec_self_mask=None, dec_enc_mask=None):

        enc_out = self.enc_embedding(x_enc)
        enc_out, attns = self.encoder(enc_out, attn_mask=enc_self_mask)

        dec_out = self.dec_embedding(x_dec)
        dec_out = self.decoder(dec_out, enc_out, x_mask=dec_self_mask, cross_mask=dec_enc_mask)

        if self.output_attention:
            return dec_out[:, -self.pred_len:, :], attns
        else:
            return dec_out[:, -self.pred_len:, :]  # [B, L, D]
