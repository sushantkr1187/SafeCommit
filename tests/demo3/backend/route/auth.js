const jwt = require("jsonwebtoken");

const JWT_SECRET = "my-super-secret-production-key";

exports.login = (req, res) => {

    const token = jwt.sign(
        { user: "admin" },
        JWT_SECRET
    );

    res.json({ token });
};