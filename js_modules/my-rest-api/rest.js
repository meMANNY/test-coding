const express = require('express');
const bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.json());

const port = 3000;
app.listen(port, () => {
    console.log(`sercver is running on port ${port}`);
});

app.get('/api/hello', (req, res) => {
    res.json({ message: 'Hello World' });
});
let todos = [];
app.get('/api/todos', (req, res) => {
    res.json(todos);
});
app.post('api/todos', (req, res) => {
    const todo = req.body;
    todos.push(todo);
    res.status(201).json(todo);
});