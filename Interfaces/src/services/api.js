const API_URL = "http://localhost:8000";

export async function uploadFile(file) {
  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch(`${API_URL}/mastering/`, {
    method: "POST",
    body: formData,
  });
  return response.json();
}

export async function getMetrics() {
  const response = await fetch(`${API_URL}/monitoring/metrics`);
  return response.json();
}
