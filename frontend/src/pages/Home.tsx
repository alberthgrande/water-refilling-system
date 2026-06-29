import { useEffect } from "react";
import { api } from "../services/api";

export default function Home() {
  useEffect(() => {
    api.get("/customers").then((response) => {
      console.log(response.data);
    });
  }, []);

  return <h1>Water Refilling Station</h1>;
}
