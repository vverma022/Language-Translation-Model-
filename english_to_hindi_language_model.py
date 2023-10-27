# -*- coding: utf-8 -*-
"""English to Hindi language Model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Qm4b8Vz-llim04a4H0SLkHkhhz3IMcir
"""

!pip install transformers -U -q

!pip install sentencepiece

from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-one-to-many-mmt")

tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-one-to-many-mmt", src_lang="en_XX")

input_text = ['be not afriad of greatness.Some are born great,Some achieve greatness,And others have greatness thrust upon them']

model_input = tokenizer(input_text, return_tensors = 'pt',padding = True, truncation = True)

#translate English to Hindi
generated_tokens = model.generate(
    **model_input,
    forced_bos_token_id = tokenizer.lang_code_to_id['hi_IN']
)

translate = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

translate