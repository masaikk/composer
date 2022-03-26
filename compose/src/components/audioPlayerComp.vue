<template>
  <div>
    <p>
      {{ audioData.audioMessage }}
    </p>
    <div>
      <audio src="" ref="mainAudioNode" @ended="endPlay"></audio>

      <el-button @click="changeAudioAndReload">change audio</el-button>
    </div>
  </div>
</template>

<script>
import { toRefs, h, reactive } from "vue";
import { ElNotification } from "element-plus";
import { useStore } from "vuex";

export default {
  name: "audioPlayerComp",
  props: ["defaultMessage", "defaultAudioURL"],
  setup(props) {
    const { defaultMessage, defaultAudioURL } = toRefs(props);

    let audioData = reactive({
      audioMessage: defaultMessage.value,
      audioURL: defaultAudioURL.value,
    });

    /*    // 获取音乐播放节点
        const mainAudioNode = ref(null);*/

    // 获取VueX
    const store = useStore();

    // get new audio url from localStorage
    const getAudioURL = () => {
      let audioInfo = store.getters.audioInfo;
      return audioInfo.audioURL;
    };

    /*    // 监听VueX里面存储的audioURL是否有变化,readonly
        const audioURLFromStore = computed(() => {
          return store.getters.audioInfo.audioURL;
        });*/

    /*    watchEffect(
          () => {
            console.log(mainAudioNode.value);

            changeAudioAndReloadSetup();
          },
          {
            flush: "post",
          }
        );*/

    /*    watch(audioURLFromStore, (nowValue, pastValue) => {
          console.log("now : " + nowValue);
          console.log("past : " + pastValue);
          // 监听之后启动reload方法，但是需要把下面的changeAudioAndReload重写至setup
        });*/

    // A function which will be used when audio play is end
    const endPlay = () => {
      // 从VueX中获取歌词信息用于在消息框中表示
      let lyrics = store.getters.getLyrics();

      ElNotification({
        title: "感谢聆听",
        message: h("i", { style: "color: teal" }, lyrics),
      });
    };

    /*    const changeAudioAndReloadSetup = (audioNode) => {
          let nowAudioURL = getAudioURL();
          console.log(audioNode.value);
          audioNode.value.src = nowAudioURL;
          audioNode.value.play();
          console.log("changeAudioAndReloadSetup " + nowAudioURL);
        };*/

    return {
      audioData,
      endPlay,
      getAudioURL,
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
