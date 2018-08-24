export class Items {
    items: Item[]
    cursor: string
}

export class Images {
    SmallImageFile: string
    MediumImageFile: string 
    LargeImageFile: string 
}

export class ItemDetails {
    UrlFriendlyName: string
    PackageSize: string
    Description: string
    IsNew: boolean
    FullDescription: string
    Unit: string
    WasPrice: number
    SmallFormatDescription: string
    SavingsAmount: number
}

export class UnitPricing {
    UnitString: string
}

export class Item  {
    name: string
    categoryLevel1: string
    categoryLevel2: string
    categoryLevel3: string
    price: number
    url: string
    images: Images
    store: string
    barcode: string
    stockcode: string
    itemDetails: ItemDetails
    unitPricing: UnitPricing
}