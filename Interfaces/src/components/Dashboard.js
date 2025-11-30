import React, { useEffect, useState } from "react";
import { getMetrics } from "../services/api";

function Dashboard() {
  const [metrics, setMetrics] = useState({});

  useEffect(() => {
    async function fetchMetrics() {
      const data = await getMetrics();
      setMetrics(data);
    }
    fetchMetrics();
  }, []);

  return (
    <div>
      <h2>Dashboard Monitoring</h2>
      <p>Latence : {metrics.latency_ms} ms</p>
      <p>Requêtes : {metrics.requests_total}</p>
      <p>Erreurs : {metrics.errors_total}</p>
    </div>
  );
}

export default Dashboard;
