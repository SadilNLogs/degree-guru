import os
import yaml

config_path = "degreegurusadil/utils/crawler.yaml"
with open(config_path, 'r') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

embedding_function_config = {
    "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": os.environ.get('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'),
    "model_name": config["index"]["openAI_embedding_model"]
}

crawler_config = config["crawler"]
text_splitter_config = config["index"]["text_splitter"]
