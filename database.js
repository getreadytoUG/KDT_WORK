import Mongoose from "mongoose";

const db_host = "mongodb+srv://wnsvy1237:Dldzmtor15@cluster0.qorzsry.mongodb.net/?retryWrites=true&w=majority"

let db;

export async function connectDB(){
    try {
        const connection = await Mongoose.connect(db_host, {
            dbName: "kdtWork"
        });
        db = connection.connection
        console.log('연결!!')
    }
    catch(error){
        console.error;
    }
}

export function getMarkets(){
    return db.collection("banapressoMarkets");
}

