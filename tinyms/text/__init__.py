# Copyright 2021 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""
This module is to support text processing for NLP tasks. It is a high performance
NLP text processing module which is developed with ICU4C and cppjieba.
"""
from mindspore.dataset.text.transforms import Lookup, JiebaTokenizer, UnicodeCharTokenizer, Ngram, \
    WordpieceTokenizer, TruncateSequencePair, \
    ToNumber, SlidingWindow, SentencePieceTokenizer, PythonTokenizer
from mindspore.dataset.text.utils import to_str, to_bytes, Vocab, SentencePieceVocab, SentencePieceModel, \
    SPieceTokenizerOutType, SPieceTokenizerLoadType

text_transform = ["Lookup", "JiebaTokenizer", "UnicodeCharTokenizer", "Ngram",
                  "WordpieceTokenizer", "TruncateSequencePair",
                  "ToNumber", "SlidingWindow", "SentencePieceTokenizer", "PythonTokenizer"]
text_utils = ["to_str", "to_bytes", "Vocab", "SentencePieceVocab", "SentencePieceModel",
              "SPieceTokenizerOutType", "SPieceTokenizerLoadType"]

__all__ = []
__all__.extend(text_transform)
__all__.extend(text_utils)
