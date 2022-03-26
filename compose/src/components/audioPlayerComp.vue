<template>
  <div>
    <p>
      {{ defaultMessage }}
    </p>
    <div>
      <audio
        controls
        src="http://119.23.182.180/azur/t1.mp3"
        ref="mainAudioNode"
        @ended="endPlay"
      ></audio>

      <el-button @click="changeAudioAndReload">change audio</el-button>
    </div>
  </div>
</template>

<script>
import { toRefs, h, computed, watch, getCurrentInstance } from "vue";
import { ElNotification } from "element-plus";
import { useStore } from "vuex";

export default {
  name: "audioPlayerComp",
  props: ["defaultMessage", "defaultAudioURL"],
  setup(props) {
    // TODO: 思考为什么这两个的proxy是readonly的属性？
    let { defaultMessage, defaultAudioURL } = toRefs(props);

    // 获取VueX
    const store = useStore();

    // get new audio url from localStorage
    const getAudioURL = () => {
      let audioInfo = store.getters.audioInfo;
      return audioInfo.audioURL;
    };

    // 监听VueX里面存储的audioURL是否有变化,readonly
    const audioURLFromStore = computed(() => {
      return store.getters.audioInfo.audioURL;
    });
    watch(audioURLFromStore, (nowValue, pastValue) => {
      console.log("now : " + nowValue);
      console.log("past : " + pastValue);
      // 监听之后启动reload方法，但是需要把下面的changeAudioAndReload重写至setup

      changeAudioAndReloadSetup();
    });

    // A function which will be used when audio play is end
    const endPlay = () => {
      ElNotification({
        title: "感谢聆听",
        message: h("i", { style: "color: teal" }, "这里是歌词"),
      });
    };

    const changeAudioAndReloadSetup = () => {
      /*      mainAudio.value.src = this.getAudioURL();
      mainAudio.value.play();*/
      // TODO: 改正一下获取不到的问题
      console.log("changeAudioAndReloadSetup");
    };

    return {
      // eslint-disable-next-line
      defaultMessage,
      // eslint-disable-next-line
      defaultAudioURL,
      endPlay,
      getAudioURL,
      // audioURLFromStore,
    };
  },
  methods: {
    changeAudioAndReload() {
      // eslint-disable-next-line
      this.$refs.mainAudioNode.src = this.getAudioURL();
      // TODO: need to fix this in setup
      console.log(
        "Reload (methods) audio in url: " + this.$refs.mainAudioNode.src
      );
      this.$refs.mainAudioNode.play();
    },
  },
};
</script>

<style scoped></style>
