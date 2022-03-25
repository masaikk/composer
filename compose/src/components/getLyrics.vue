<template>
  <div>
    <div>占位</div>
    <div>
      <el-button @click="sendAjax">sendTO</el-button>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import axios from "axios";

export default {
  name: "getLyrics",
  setup() {
    let lyrics = ref("this is a sentence");
    let developFlag = ref(true);
    const developmentURL = "http://127.0.0.1:8000/form/getAudioPath/";

    const sendAjax = () => {
      axios
        .get(developmentURL)
        .then((response) => {
          /*        alert(
          "".concat(
            response.data,
            "\r\n",
            response.status,
            "\r\n",
            response.statusText,
            "\r\n",
            response.headers,
            "\r\n",
            response.config
          )*/
          console.log("Got audio url : " + response.data);
        })
        .catch((err) => {
          alert(err);
        });
    };

    return {
      lyrics,
      developFlag,
      sendAjax,
    };
  },
};
</script>

<style scoped></style>
