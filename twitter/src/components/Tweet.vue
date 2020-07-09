<template>
  <div>
    <div class="wrapper" :class="{ reply: this.is_reply || this.has_reply }">
      <div class="profile-image">
        <div v-if="status.user.profile_image">
          <img :src="status.user.profile_image" class="circle-border"/>
        </div>
        <div v-else>
          <div class="circle-border initials">
            {{ userInitials }}
          </div>
          <div v-if="has_reply" class="line-container">
            <div class="line">
            </div>
          </div>
        </div>
      </div>
      <div class="content">
        <div class="info">
          <TweetInfo :status="status" />
        </div>
        <div class="content">
          {{ status.text }}
          <Quote v-if="status.quoted_status" :status="status.quoted_status" />
        </div>
        <TweetActionBar :status="status" />
      </div>
    </div>
  </div>
</template>

<script>
import Quote from './Quote.vue';
import TweetActionBar from './TweetActionBar.vue';
import TweetInfo from './TweetInfo.vue';

export default {
  name: 'Tweet',
  components: {
    Quote,
    TweetActionBar,
    TweetInfo,
  },
  props: {
    status: {
      type: Object,
      required: true,
    },
    is_reply: {
      type: Boolean,
      required: false,
    },
    has_reply: {
      type: Boolean,
      required: false,
    },
  },
  computed: {
    userInitials() {
      return this.status.user.name.match(/\b(\w)/g).join('');
    },
  },
};
</script>

<style lang="scss" scoped>
.circle-border {
  border-radius: 50%;
  width: 50px;
  height: 50px;
  min-width: 50px;
  min-height: 50px;
}
.initials {
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 700;
  font-size: 20px;
  background-color: rgb(85, 168, 250);
}
.wrapper {
  display: flex;
  flex-direction: row;
  // border: 1px solid lightgrey;
  padding: 15px;
  padding-bottom: 5px;
  border-radius: 15px;
  background-color: #fff;
  box-shadow: 0px 2px 2px 0px rgba(200,200,200,0.5);
  margin: 5px 0 10px 0;
}
.reply {
  box-shadow: none;
  padding: 0 15px;
  margin: 0 0;
}
.profile-image {
  margin: 0 15px 0 0;
}
.info {
  display: flex;
  flex-direction: row;
}
.content {
  width: 100%;
  margin-top: 5px;
}
.line {
  border: 1px solid lightskyblue;
  height: 30px;
  width: 0;
  margin: 5px auto;
}
.line-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  flex: 1;
  min-height: 100%;
}
</style>
