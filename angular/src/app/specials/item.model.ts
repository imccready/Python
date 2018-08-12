export interface Items {
    items: Item[]
}

export interface IItem { 
    name: string
}
export class Item implements IItem {
    constructor(public name: string) {

    }
   
    
}