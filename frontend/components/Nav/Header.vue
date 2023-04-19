<template>
    <div class="Header">
        <v-navigation-drawer
        v-model="drawer"
        temporary
      >
        <v-list-item
          prepend-icon="$account"
          v-if="userfetch"
        >
        <NuxtLink to="/account" class="hover:text-blue">{{ auth.user?.data.user.name }}</NuxtLink>
      </v-list-item>

        <v-divider></v-divider>
        <v-list density="compact" nav>
            <NuxtLink :to="item.href" v-for="item in tabs" :key="item.name">
                <v-list-item :prepend-icon="item.icon" :title="item.name" :value="item.name"></v-list-item>
            </NuxtLink>
        </v-list>
      </v-navigation-drawer>
        <v-app-bar
            color="primry"
            elevation="4"
            :collapse="false"
          >
            <template v-slot:prepend 
            >
              <v-app-bar-nav-icon @click.stop="drawer= true" class="d-flex d-sm-none"></v-app-bar-nav-icon>
            </template>
            
            <v-app-bar-title>
                <NuxtLink to="/" class="text-decoration-none"><b>Shramik</b></NuxtLink>
            </v-app-bar-title>
                    <!-- Navigation Tabs top tabs -->
            <v-tabs
                align-tabs="center"
                class="d-none d-sm-flex"
            ><v-row justify-md="center" align="center">
              <Location />
              <div v-for="(item, i) in tabs" :key="i">
                  <NuxtLink :to="item.href">
                      <v-tab :prepend-icon="item.icon" :value="i">
                          {{ item.name }}
                      </v-tab>
                  </NuxtLink>
              </div>
            </v-row>
            </v-tabs>
            <v-spacer></v-spacer>
            <section v-if="auth.loggedIn==false && userfetch == true" class="mx-3">
              <NuxtLink to="/auth/sign-in">
                <v-btn variant="tonal" color="white">
                  Sign In
                </v-btn>
              </NuxtLink>
                
            </section>
            <section v-if="auth.loggedIn">
                <!-- Account panel -->
                 <v-menu
                    location="end"
                    transition="scale-transition"
                    >
                    <template v-slot:activator="{ props }">
                        <v-btn icon v-bind="props">
                            <v-icon icon="$account"></v-icon>
                        </v-btn>
                    </template>

                    <v-list>
                        <v-list-item
                        v-for="(item, i) in AccountActions"
                        :key="i"
                        >
                        <NuxtLink :to="item.href">
                          <v-list-item-title>{{ item.name }}</v-list-item-title>
                        </NuxtLink>
                        </v-list-item>
                        <v-divider></v-divider>
                        <v-list-item @click.prevent="logout">
                          <v-list-item-title >Log out</v-list-item-title>
                        </v-list-item>
                    </v-list>
                </v-menu>

                <!-- Notofication extension menu -->
                <v-menu
                    v-model="notificationPanel"
                    location="end"
                    transition="scale-transition"
                >
                    <template v-slot:activator="{ props }">
                        <v-btn icon v-bind="props" >
                            <v-icon icon="$notification"></v-icon>
                        </v-btn>
                    </template>
                    <v-card min-width="300">
                        <v-list>
                            <v-list-item v-for="item in notifications" :key="item.href" :prepend-icon="item.icon" :title="item.title" :value="item.tag">
                            </v-list-item>
                        </v-list>
                        <v-card-actions>
                        <v-divider></v-divider>
                            <v-btn
                                variant="text"
                                @click="notificationPanel = false"
                            >
                                Close
                            </v-btn>
                        </v-card-actions>
                    </v-card>
                    </v-menu>
                
                <v-btn icon>
                  <v-icon icon="$message"></v-icon>
                </v-btn>
            </section>
    
          </v-app-bar>
    </div>
</template>

<script setup>
import {useCitiesStore} from '@/stores/cities';
import { storeToRefs } from 'pinia';
const drawer = ref(false);
const notificationPanel = ref(false);

const {$auth: auth, $sanctumAuth} = useNuxtApp();
const citiesStore = useCitiesStore();

// const props = defineProps({
//     offsetTop: {
//         type: Object,
//         required: true
//     }
// })

const userfetch = ref(false);
async function user(){
  try {
    await $sanctumAuth.getUser();
    userfetch.value = true;
    console.log("userfetch - ", userfetch);
  } catch (error) {
    console.log(error);
  }
}

const tabs = [
    {
        name: "Home",
        description: "Get all of your questions answered in our forums or contact support.",
        href: "/",
        icon: '$home',
    },
    {
        name: "Network",
        description: "Learn how to maximize our platform to get the most out of it.",
        href: "/network",
        icon: '$group',
    },
    {
        name: "WorkPlace",
        description: "See what meet-ups and other events we might be planning near you.",
        href: "/workplace",
        icon: '$jobs',
    },
  ]

  const AccountActions = [
    {
        name:'My Profile',
        href:'/account',
    },
    {
        name:'Settings',
        href:'#',
    },
    {
        name:'Help',
        href:'#',
    },
  ];

  const notifications = [
    {
        title: "Sanket connected to your network",
        href: "#",
        icon: '$group',
        tag: 'network'
    },
    {
        title: "Contractor mr.Savant posted new Project",
        href: "#",
        icon: '$jobs',
        tag: 'WorkPlace'
    },
        {
        title: "You have new message from mr.sawant",
        href: "#",
        icon: '$group',
        tag: 'Message'
    },
    {
        title: "Find new Jobs in Thane",
        href: "#",
        icon: '$jobs',
        tag: 'Jobs'
    },
  ]

  async function logout(){
    await $sanctumAuth.logout(logout)
    .then((res)=>{
      console.log(res);
    })
    .catch((error)=>{
      console.log(error);
    })
  }

  onMounted(()=>{
    user(),
    citiesStore.setCities();
  })

</script>