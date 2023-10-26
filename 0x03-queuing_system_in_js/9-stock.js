import express from 'express';
import redis from 'redis';
import {promisify} from 'util';

const client = redis.createClient();

client.on('connect', () => {
    console.log(`client connected to server`);
})

const get = promisify(client.get).bind(client);

const port = 1245;

const listProducts = [
    {
        id: 1,
        name: 'Suitcase 250',
        price: 50,
        stock: 4,
        initialAvailableQuantity: 4
    },
    {
        id: 2,
        name: 'Suitcase 450',
        price: 100,
        stock: 10,
        initialAvailableQuantity: 10
    },
    {
        id: 3,
        name: 'Suitcase 650',
        price: 350,
        stock: 2,
        initialAvailableQuantity: 2
    },
    {
        id: 4,
        name: 'Suitcase 1050',
        price: 550,
        stock: 5,
        initialAvailableQuantity: 5
    }
]

function getElementById(id){ 
    return listProducts.filter(product => product.id == id);
}

function reserveStockById(itemId, stock) {
    client.set(itemId, stock);
}

async function getCurrentReservedStockById(itemId){
    const stock = await get(itemId);
    return stock;
}

const server = express();


server.get('/list_products', (req, res) => {
    return res.json(listProducts);
});

server.get('/list_products/:itemId', async(req, res) => {
    const itemId = Number(req.params.itemId);

    const stock = await getCurrentReservedStockById(itemId);
    console.log(stock);
    const item = getElementById(itemId);

    if (item.length > 0) {
        item.currentQuantity = stock;
        res.json(item);
        return;
    }
    res.status(404).json({ status: 'Product not found' });
});

server.get('/reserve_product/:itemId', async(req, res) => {
    const itemId = req.params.itemId;

    const item = getElementById(itemId);

    if (item.length < 0) {
        res.json({status: 'Product not found'});
        return;
    }

    const stock = await getCurrentReservedStockById(itemId);
    if (stock < 1) {
        res.json({status: 'Not enough stock available'});
        return;
    }

    reserveStockById(itemId, stock);
    res.json({status: `reservation confirmed ${itemId}`});
});

server.listen(port, () => {
    listProducts.forEach((product) => reserveStockById(product.id,
        product.initialAvailableQuantity));
});
