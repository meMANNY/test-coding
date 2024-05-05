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

const data = [
    { id: 1, name: 'John Doe', age: 25 },
    { id: 2, name: 'Jane Doe', age: 30 },
    { id: 3, name: 'Bob Smith', age: 40 },
    { id: 4, name: 'Alice Brown', age: 20 },
    { id: 5, name: 'Mike Johnson', age: 35 },
    { id: 6, name: 'Sara Lee', age: 28 },
    { id: 7, name: 'David Green', age: 45 },
    { id: 8, name: 'Emily Davis', age: 32 },
    { id: 9, name: 'Tom Wilson', age: 27 },
    { id: 10, name: 'Linda Wilson', age: 33 }
  ];

const pageSize = 3;
// app.get('/api/users', (req, res) => {
//     const pageNumber = req.query.page || 1;
//     const startIndex = (pageNumber - 1) * pageSize;
//     const endIndex = pageNumber + pageSize;
//     const users = data.slice(startIndex, endIndex);
//     res.json({users, total: data.length});
// });

const pagination = (pageSize) =>{
    return (req,res,next) =>{
        const pageNumber = req.query.page || 1;
        const startIndex = (pageNumber - 1) * pageSize;
        const endIndex = pageNumber + pageSize;
        
        req.pagination ={
        page: pageNumber,
        limit: pageSize,
        startIndex,
        endIndex, 
        };
        next();
    };
};
app.get('/api/users', pagination(10), (req, res) => {
    const {startIndex, endIndex} = req.pagination;
    const users = data.slice(startIndex, endIndex);

    res.json({users,total: data.length});  
});