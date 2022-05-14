<template>
  <div class="common-layout">
    <el-container>
      <el-header>
        <slot name="top-bar-header"></slot>
      </el-header>
      <el-container>
        <el-aside width="200px">
          <slot name="top-bar-aside"></slot>
        </el-aside>
        <el-container>
          <el-main id="main-root">
            <slot name="top-bar-main"></slot>
          </el-main>
          <el-footer>
            <slot name="top-bar-footer"></slot>
          </el-footer>
        </el-container>
      </el-container>
    </el-container>
  </div>
</template>

<script setup>
import { ref, reactive } from "vue";
import { useStore } from "vuex";

export default {
  name: "topBar",
};
</script>

<style scoped></style>
