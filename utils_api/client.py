import httpx

class ServerestClient:
    def __init__(self, base_url="https://serverest.dev"):
        self.client = httpx.Client(base_url=base_url)
        self.token = None

    def set_token(self, token):
        self.client.headers.update({"Authorization": token})

    def post(self, path, data):
        return self.client.post(path, json=data)

    def get(self, path):
        return self.client.get(path)

    def delete(self, path):
        return self.client.delete(path)

    def put(self, path, data):
        return self.client.put(path, json=data)
