// store.js
import { writable } from 'svelte/store';

// Define a writable store with an initial value
export let active_file = writable('');