import express from "express";
import cors from "cors";
import morgan from "morgan";
import banaRouter from "./banaRouter.js"
import { connectDB } from "./database.js";

const app = express();
app.use(morgan("dev"))
app.use(express.json());
app.use(cors());

app.use("/banapresso", banaRouter);

app.use((req, res, next) => {
    res.sendStatus(404);
})

connectDB().then(() => {
    app.listen(8080);
}).catch(console.error);


