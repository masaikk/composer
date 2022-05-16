import serviceAxios from "@/apis/networks";

export const getComments = (params) => {
  return serviceAxios({
    method: "get",
    url: "/user/get_comments/",
    params,
  });
};

export const addCommentById = (params) => {
  return serviceAxios({
    method: "get",
    url: "/user/add_comment/",
    params,
  });
};

export const getMyInfoByUid = (params) => {
  return serviceAxios({
    method: "get",
    url: "/user/user_info/",
    params,
  });
};

export const generateMelody = (params) => {
  return serviceAxios({
    method: "get",
    url: "/lyrics/generateAudio/",
    params,
  });
};

export const getInstrumentsList = (params) => {
  return serviceAxios({
    method: "get",
    url: "/lyrics/getInstruList/",
    params,
  });
};

export const getLogsByUid = (params) => {
  return serviceAxios({
    method: "get",
    url: "/user/get_log/",
    params,
  });
};
