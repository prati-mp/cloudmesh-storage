from cloudmesh.storage.provider.gdrive.Provider import \
    Provider as GdriveProvider
from cloudmesh.storage.provider.box.Provider import Provider as BoxProvider
from cloudmesh.storage.StorageABC import StorageABC


class Provider(StorageABC):

    #
    # TODO: use whate we implemented in the StorageABC
    #
    def __init__(self, cloud=None, config="~/.cloudmesh/cloudmesh4.yaml"):
        super(Provider, self).__init__(cloud=cloud, config=config)
        self.provider = None
        if self.kind == "gdrive":
            provider = GdriveProvider()
        elif self.kind == "box":
            provider = BoxProvider()
        else:
            raise ValueError(f"Storage provider {cloud} not yet supported")
        return provider

    def list(self, parameter):
        print("list", parameter)
        provider = self._provider(self.service)

    def delete(self, filename):
        print("delete filename")
        provider = self._provider(self.service)
        provider.delete(filename)

    def get(self, service, filename):
        print("get", service, filename)
        provider = self._provider(service)
        provider.get(filename)

    def put(self, service, filename):
        print("put", service, filename)
        provider = self._provider(service)
        provider.put(filename)
