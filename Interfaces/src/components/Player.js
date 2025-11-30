import React from "react";

function Player({ src }) {
  return (
    <div>
      <h3>Lecteur Audio</h3>
      <audio controls>
        <source src={src} type="audio/wav" />
        Votre navigateur ne supporte pas l’audio.
      </audio>
    </div>
  );
}

export default Player;
