const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());

// Temporary storage
let users = [];

// GET all users
app.get('/users', (req, res) => {
    res.json(users);
});

// POST create user
app.post('/users', (req, res) => {
    const newUser = req.body;

    users.push(newUser);

    res.json({
        message: 'User created',
        user: newUser
    });
});

// PUT update user
app.put('/users/:id', (req, res) => {
    const userId = req.params.id;
    const updatedUser = req.body;

    users[userId] = updatedUser;

    res.json({
        message: `User with ID ${userId} updated`,
        updatedUser
    });
});

// DELETE user
app.delete('/users/:id', (req, res) => {
    const userId = req.params.id;

    users.splice(userId, 1);

    res.json({
        message: `User with ID ${userId} deleted`
    });
});

app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});