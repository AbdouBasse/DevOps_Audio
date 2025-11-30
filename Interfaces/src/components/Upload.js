import React, { useState } from "react";
import { uploadFile } from "../services/api";

function Upload() {
  const [file, setFile] = useState(null);

  const handleUpload = async () => {
    if (file) {
      const response = await uploadFile(file);
      alert("Fichier traité : " + response.processed_file);
    }
  };

  return (
    <div>
      <h2>Uploader un fichier audio</h2>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Envoyer</button>
    </div>
  );
}

export default Upload;
