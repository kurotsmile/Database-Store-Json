

import express from "express";
import { Low } from "lowdb";
import { JSONFile } from "lowdb/node";
import _ from "lodash";

const app = express();
app.use(express.json());

app.get("/", (req, res) => {
  res.send(`
    <h1>Database Store Json</h1>
    <ul>
      <li><a href="/users">Users (l=en)</a></li>
      <li><a href="/user/get">Get user (id,l=en)</a></li>
      <li><a href="/songs">All Song</a></li>
    </ul>
  `);
});

app.get("/users", async (req, res) => {
  let l =req.query.l;
  if(l==null) l="en";
  const adapter_user = new JSONFile("user-"+l+".json");
  const dbUser = new Low(adapter_user, { all_item: [] });
  await dbUser.read();
  const randomUsers = _.sampleSize(dbUser.data.all_item, 20);
  res.json(randomUsers);
});

app.get("/user/get", async (req, res) => {
  let id =req.query.id;
  let l=req.query.l;
  if(l==null) l="en";
  const adapter_user = new JSONFile("user-"+l+".json");
  const dbUser = new Low(adapter_user, { all_item: [] });
  await dbUser.read();
  const user = dbUser.data.all_item.find(u => u.id_import === id);
  res.json(user);
});

app.get("/songs", async(req, res) => {
  const adapter_song = new JSONFile("song.json");
  const dbSong = new Low(adapter_song, { all_item: [] });
  await dbSong.read();
  const randomSong= _.sampleSize(dbSong.data.all_item, 20);
  res.json(randomSong);
});

app.listen(3000, () => {
  console.log("🚀 Server running at http://localhost:3000");
});
