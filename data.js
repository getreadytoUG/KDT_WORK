import Mongoose     from "mongoose";
import { getMarkets, connectDB } from "./database.js";

export async function getAll(){
    try{
        await connectDB();
        const data = await getMarkets().find().toArray();
        console.log(data)
        return data
    }
    catch{
        console.error;
    }
}