import axios from "axios";
const serviceAxios = axios.create({
  baseURL: "http://127.0.0.1:8000",
  timeout: 5000,
});

serviceAxios.interceptors.request.use(
  (config) => {
    console.log(config);
    return config;
  },
  (error) => {
    Promise.reject(error);
  }
);

serviceAxios.interceptors.response.use(
  (res) => {
    console.log(res);
    return res;
  },
  (error) => {
    console.log(error);
  }
);

export default serviceAxios;
