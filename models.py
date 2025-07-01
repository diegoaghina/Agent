from smolagents.models import InferenceClientModel
from huggingface_hub import InferenceClient
import config_keys

class HfApiModel(InferenceClientModel):
    def __init__(
        self,
        model_id: str,
        temperature: float = 0.5,
        max_tokens: int = 1024,
        custom_role_conversions=None,
    ):
        

        token = config_keys.hugging_face_api_key
        if token is None:
            raise ValueError("Please set your HUGGINGFACEHUB_API_TOKEN environment variable.")

        client = InferenceClient(model=model_id, token=token)

        super().__init__(
            client=client,
            model_id=model_id,
            temperature=temperature,
            max_tokens=max_tokens,
            custom_role_conversions=custom_role_conversions,
        )
