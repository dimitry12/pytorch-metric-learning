from .base_metric_loss_function import BaseMetricLossFunction, MultipleLosses
from .angular_loss import AngularLoss
from .arcface_loss import ArcFaceLoss
from .contrastive_loss import ContrastiveLoss
from .fast_ap_loss import FastAPLoss
from .generic_pair_loss import GenericPairLoss
from .lifted_structure_loss import GeneralizedLiftedStructureLoss
from .margin_loss import MarginLoss
from .multi_similarity_loss import MultiSimilarityLoss
from .nca_loss import NCALoss
from .normalized_softmax_loss import NormalizedSoftmaxLoss
from .n_pairs_loss import NPairsLoss
from .proxy_losses import ProxyNCALoss
from .signal_to_noise_ratio_losses import SignalToNoiseRatioContrastiveLoss
from .soft_triple_loss import SoftTripleLoss
from .triplet_margin_loss import TripletMarginLoss
from .weight_regularizer_mixin import WeightRegularizerMixin