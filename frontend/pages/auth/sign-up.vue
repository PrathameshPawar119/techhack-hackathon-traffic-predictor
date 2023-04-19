<template>
    <v-container fluid>
        <v-row justify="center" class="pa-2">
            <v-col cols="12" sm="8" md="6" lg="4" class="rounded-xl pa-4 mt-10 text-center">
                <v-card class="mx-auto rounded-xl" elevation="4" variant="outlined">
                    <div class="ma-4 rounded-xl">
                        <v-card-title>
                            <h1 class="ma-3" style="font-size:54px">Shramik</h1>
                        </v-card-title>
                        <v-card-subtitle>
                            <h2 class="text-body-1 mb-3">We make your work done, sign-up!</h2>
                        </v-card-subtitle>
                            <v-text-field
                                v-model="formData.email"
                                label="Email"
                                placeholder="Email"
                                type="email"
                                name="email"
                                required
                                :error-messages="v$.email.$errors[0] ? v$.email.$errors[0].$message : ''"
                                variant="outlined"
                                :disabled="formData.otpSent"
                                class="mt-4 mb-0"
                                color="success"
                            >
                            </v-text-field>
                            <v-btn
                            v-if="formData.otpSent==false && formData.verified==false"
                                color="primary"
                                class="p-2 mb-3"
                                @click.prevent="sendOtp"
                                >Send OTP</v-btn
                            >
                    </div>
                    <div v-if="formData.otpSent==true && formData.verified==false">
                        <v-text-field
                            v-model="formData.otp"
                            label="Verify OTP"
                            placeholder="Enter your otp"
                            name="VerifyOTP"
                            type="number"
                            hide-spin-buttons
                            variant="outlined"
                            required
                            color="success"
                            class="mx-4"
                            :error-messages="v$.otp.$errors[0] ? v$.otp.$errors[0].$message : ''"
                            ></v-text-field>
                        <v-btn
                            color="primary"
                            class="p-2 mb-3"
                            @click.prevent="verifyOtp"
                            >Verify OTP</v-btn
                        >
                    </div>

                    <div v-if="formData.verified == true">
                    <LazyAuthSignUp :formData="formData" />
                    </div>

                    <v-row class="my-4" justify="space-around" v-if="formData.verified == false">
                        <v-btn
                            variant="text"
                            size="small"
                            :to="{ path: '/auth/sign-in' }"
                            >Sign-In</v-btn
                        >
                        <v-btn
                            variant="text"
                            size="small"
                            :to="{ path: '/auth/reset' }"
                            >Forgot password</v-btn
                        >
                    </v-row>
                </v-card>
            </v-col>
        </v-row>
    </v-container>

</template>

<script setup>
import { useVuelidate } from "@vuelidate/core";
import { required, email, helpers } from "@vuelidate/validators";
import { reactive } from 'vue';

const {$sanctumAuth} = useNuxtApp();
const { $useFetchApi: useFetchApi } = useNuxtApp();

const formData = reactive({
    email: null,
    otp:null,
    otpSent: false,
    verified: false,
})

const rules = computed(() => {
  const localRules = {
    email: {
      required: helpers.withMessage("email is required", required),
      email: helpers.withMessage("must be a valid email", email),
    },
  };
  if (formData.otpSent) {
    // if billing is not the same as shipping, require it
    localRules.otp = {
      required: helpers.withMessage("otp is required", required),
    };
  }
  return localRules;
});

const v$ = useVuelidate(rules, formData, {$lazy: true})
definePageMeta({
    middleware: ["guest"]
})

useHead({
    title: "SignUp"
})




async function sendOtp(){
    const formvalid = await v$.value.$validate()
    if(formvalid){
        const { pending, data, error, refresh } = await useFetchApi("sendotp", {
            method: "POST",
            body: {
                email: formData.email,
                type: "register",
            },
        });

        if (data.value) {
            formData.otpSent = true;
            console.log("OTP sent");
        }
        else if(error.value){
            console.log("OTP sent Error");
        }
    }
}

async function verifyOtp(){
      const { pending, data, error, refresh } = await useFetchApi("verifyotp", {
            method: "POST",
            body: {
                email: formData.email,
                otp: formData.otp,
        }

    });
    if (data.value) {
        formData.verified = true;
        console.log("OTP Verified");
    }
    else if(error.value){
        console.log("OTP verify Error");
    }
}
</script>
