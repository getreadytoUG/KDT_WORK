import { response } from "express";
import * as marketRepository from "./data.js";

export async function getMarket(req, res){
    try{
        const data = await marketRepository.getAll();
        console.log(data)
        res.status(200).json(data);
    }
    catch{
        console.error;
    }
}