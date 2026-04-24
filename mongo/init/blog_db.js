const blogDb = db.getSiblingDB("blog_db");

const mongoUser = process.env.MONGO_APP_USER;
const mongoPassword = process.env.MONGO_APP_PASSWORD;

blogDb.createUser({
  user: mongoUser,
  pwd: mongoPassword,
  roles: [{ role: "readWrite", db: "blog_db" }]
});

const schema = {
  bsonType: "object",
  required: ["titre", "auteur", "vues"],
  properties: {
    titre: {
      bsonType: "string",
      description: "'titre' doit être une chaîne"
    },
    auteur: {
      bsonType: "string",
      description: "'auteur' doit être une chaîne"
    },
    vues: {
      bsonType: "int",
      minimum: 0,
      description: "'vues' doit être un entier >= 0"
    }
  }
};

blogDb.createCollection("posts", {
  validator: { $jsonSchema: schema },
  validationLevel: "strict",
  validationAction: "error"
});

blogDb.posts.insertMany([
  { titre: "Bienvenue sur le blog", auteur: "Alice", vues: NumberInt(120) },
  { titre: "Découverte de MongoDB", auteur: "Bob", vues: NumberInt(85) },
  { titre: "Docker pour débutants", auteur: "Claire", vues: NumberInt(64) },
  { titre: "Sécuriser ses conteneurs", auteur: "David", vues: NumberInt(47) },
  { titre: "Publier sur Docker Hub", auteur: "Emma", vues: NumberInt(30) }
]);

