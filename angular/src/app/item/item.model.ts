export interface IItem { 
    name: string
    category: string
    sub_category: string
    price: number
    url: string
    image_url: string
    store: string
    barcode: string
    product_code: string
}
export class Item implements IItem {
    name: string;
    category: string;
    sub_category: string;
    price: number;
    url: string;
    image_url: string;
    store: string;
    barcode: string;
    product_code: string;
    
    constructor() {

    }
   
    
}