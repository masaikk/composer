<template>
  <div>
    <div>
      <div>{{ mainPageInfo.mainName }}</div>
      <div>
        <h6>{{ mainPageInfo.mainPageMessage }}</h6>
      </div>
    </div>
    <div>
      <get-lyrics></get-lyrics>
    </div>
    <div>
      <audio-player-comp
        :defaultMessage="audioInfo.defaultMessage"
        :defaultAudioURL="audioInfo.defaultAudioURL"
      ></audio-player-comp>
    </div>
  </div>
</template>

<script>
import { reactive, onBeforeMount } from "vue";
import audioPlayerComp from "@/components/audioPlayerComp";
import getLyrics from "@/components/getLyrics";

export default {
  name: "composeMain",
  setup() {
    let mainPageInfo = reactive({
      mainName: "Composer",
      mainPageMessage: "powered by HJQ",
      mainPageEmail: "201830660420@mail.scut.edu.cn",
    });

    let audioInfo = reactive({
      defaultMessage: "default message",
      defaultAudioURL: "http://119.23.182.180/azur/t1.mp3",
    });

    const setAudioURL2localStorge = () => {
      localStorage.setItem("audioURL", audioInfo.audioURL);
    };

    onBeforeMount(() => {
      setAudioURL2localStorge();
    });

    return {
      mainPageInfo,
      audioInfo,
    };
  },
  components: {
    audioPlayerComp,
    getLyrics,
  },
};
</script>

<style scoped></style>
