<template>
  <div>
    <h3>精彩评论</h3>
    <div id="comment-list-holder">
      <el-table :data="commentsList.data" stripe id="comment-data">
        <el-table-column prop="cid" label="cid" />
        <el-table-column prop="uid" label="uid" />
        <el-table-column prop="comment" label="评论" />
        <el-table-column prop="time" label="时间" />
      </el-table>
      <el-button @click="flushCommentsList">刷新评论</el-button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { reactive, onBeforeMount } from "vue";
import { ElMessage } from "element-plus";

export default {
  name: "commentView",
  setup() {
    let commentsList = reactive({
      data: [],
    });

    onBeforeMount(() => {
      flushCommentsList();
    });

    const flushCommentsList = () => {
      axios.get("http://127.0.0.1:8000/user/get_comments").then((res) => {
        ElMessage({
          showClose: true,
          message: "一共有" + res.data.commentData.length + "条评论记录！",
          type: "success",
        });
        commentsList.data = res.data.commentData;
        console.log(commentsList.data);
      });
    };

    return {
      commentsList,
      flushCommentsList,
    };
  },
};
</script>

<style scoped></style>
