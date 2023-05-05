from shipping.models import Address,Origin

# "Street 1, 10115 Berlin, Germany"
class AddressImportService:
    def __retrieveAddress(self,street:str,origin:Origin)->Address:
        streetNumber=street.split()[1]
        address,_ =Address.objects.get_or_create(street=streetNumber,origin=origin)
        
        return address

    def __retrieveOrigin(self,origin:str)->Origin:
        origin = origin.split(", ")
        country=origin[1]
        [zipCode,city]=origin[0].split()
        savedOrigin,_=Origin.objects.get_or_create(country=country,city=city,zipCode=zipCode)

        return savedOrigin

    def handleAddressFetch(self,fullAddress:str)->Address:
        address = fullAddress.split(", ", 1)
        street=address[0]
        origin=address[1]
        savedOrigin=self.__retrieveOrigin(origin=origin)
        savedAddress=self.__retrieveAddress(street=street,origin=savedOrigin)

        return savedAddress