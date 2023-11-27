import express from "express";
import * as Controller from "./controller.js"

const router = express.Router();

router.get("/markets", Controller.getMarket);

export default router;