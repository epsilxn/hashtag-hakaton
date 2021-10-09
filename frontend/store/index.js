import axios from "axios"
export const state = () => ({
    token: null,
    is_staff: null
})

export const actions = {
    auth(context, token) {
        context.commit('setToken', token)
    },
    setStaff(context, staff) {
        context.commit('setStaff', staff)
    }
}


export const mutations = {
    setToken(state, token) {
        state.token = token
    },
    setStaff(state, staff) {
        state.is_staff = staff
        console.log(state.is_staff)
    }
}