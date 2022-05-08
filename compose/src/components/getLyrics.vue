<template>
  <div id="gen-comp-root">
    <div id="gen-comp-head">发送音乐信息</div>

    <div id="gen-comp-main">
      <el-select
        v-model="selectedInstrumentID"
        class="m-2"
        placeholder="Select"
      >
        <el-option
          v-for="instru in instrumentList.InsList"
          :key="instru.value"
          :label="instru.name"
          :value="instru.value"
        />
      </el-select>
      <el-input v-model="lyrics" placeholder="Please input" clearable />
    </div>
    <div id="gen-comp-foot">
      <el-button @click="sendMelodyGenerateInfo">合成旋律！</el-button>
    </div>
  </div>
</template>

<script>
import { reactive, ref, onBeforeMount } from "vue";
import axios from "axios";
import { useStore } from "vuex";
import { ElMessage } from "element-plus";

export default {
  name: "getLyrics",
  setup() {
    const store = useStore();
    let lyrics = ref("This is a sentence and attention is all your need .");
    let developFlag = ref(true);

    const developmentURL = "http://127.0.0.1:8000/lyrics/getAudioPath/";
    const developmentInstruListURL =
      "http://127.0.0.1:8000/lyrics/getInstruList/";

    let selectedInstrumentID = ref("3");
    const sendMelodyGenerateInfo = () => {
      ElMessage({ showClose: true, message: "合成请求已经发送！" });
      axios
        .get(developmentURL, {
          params: {
            lyrics: lyrics.value,
            instrumentID: selectedInstrumentID.value,
            uid: store.getters.getUid(),
          },
        })
        .then((response) => {
          console.log(response.data);
          store.commit("setAudioURLAndFlag", {
            audioURL: response.data.music_url,
          });
          store.commit("setLyrics", lyrics);

          ElMessage({
            showClose: true,
            message: "旋律已经生成！\n 请点击下方按钮播放！",
            type: "success",
          });
        })
        .catch((err) => {
          alert(err);
          ElMessage({
            showClose: true,
            message: "抱歉，旋律生成错误！\n请稍后重试！",
            type: "error",
          });
        });
    };
    const showInfoFromStore = () => {
      let info = store.getters.audioInfo;
      console.log(info);
    };
    let instrumentList = reactive({ InsList: [] });
    const getInstruList = () => {
      axios.get(developmentInstruListURL).then((res) => {
        instrumentList.InsList = Array.from(res.data.INSTRUMENT_MAP);
        // instrumentList.InsList = ["1", "2", "3"];
        // console.log(instrumentList.InsList);
        console.log("乐器数据更新成功");
      });
    };

    onBeforeMount(() => {
      getInstruList();
    });

    return {
      lyrics,
      developFlag,
      sendMelodyGenerateInfo,
      showInfoFromStore,
      instrumentList,
      selectedInstrumentID,
    };
  },
};
</script>

<style scoped></style>
