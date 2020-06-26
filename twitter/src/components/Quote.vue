<template>
  <div class="quote">
    <div>
      <div class="row px-3 my-2">
        <div class="col">
          <div class="row mx-0 inline-elements">
            <div class="">
              <div v-if="status.user.profile_image">
                <img :src="status.user.profile_image" class="circle-border"/>
              </div>
              <div v-else class="">
                <div class="circle-border initials">
                  {{ userInitials }}
                </div>
              </div>
            </div>
            <div class="username font-weight-bold">
              {{ status.user.name }}
            </div>
            <div v-if="status.user.verified">
              ✔
            </div>
            <div>
              @{{ status.user.screen_name }}
            </div>
            <div>
              • {{ timeDiff }} ago
            </div>
          </div>
          <div class="row">
            <div class="col">
            {{ status.text }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const humanizeDuration = require('humanize-duration');

export default {
  name: 'Quote',
  props: {
    status: {
      type: Object,
      required: true,
    },
  },
  computed: {
    timeDiff() {
      const createdAt = new Date(this.status.created_at);
      const diff = new Date() - createdAt;
      return humanizeDuration(diff, { largest: 1 });
    },
    userInitials() {
      return this.status.user.name.match(/\b(\w)/g).join('');
    },
  },
};
</script>

<style lang="scss" scoped>
.circle-border {
  border-radius: 50%;
  width: 20px;
  height: 20px;
  min-width: 20px;
  min-height: 20px;
  margin-right: 5px;
}
.initials {
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 700;
  font-size: 10px;
  background-color: rgb(85, 168, 250);
}
.inline-elements {
  display: flex;
  align-items: center;
}
.quote {
  border: solid 1px lightgray;
  border-radius: 15px;
}
</style>
