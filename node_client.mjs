// Minimal client for the JSONPlaceholder demo REST API.
//
// Usage:
//   node node_client.mjs
//
// Requires Node 18 or newer for the global fetch implementation.

const BASE_URL = "https://jsonplaceholder.typicode.com";
const TIMEOUT_MS = 10_000;

async function request(path, options = {}) {
  const response = await fetch(`${BASE_URL}${path}`, {
    ...options,
    headers: { Accept: "application/json", ...options.headers },
    signal: AbortSignal.timeout(TIMEOUT_MS),
  });
  return response;
}

async function listPosts({ userId, limit = 3 } = {}) {
  const query = userId === undefined ? "" : `?userId=${encodeURIComponent(userId)}`;
  const response = await request(`/posts${query}`);
  if (!response.ok) throw new Error(`list posts failed: ${response.status}`);
  const posts = await response.json();
  return posts.slice(0, limit);
}

async function getPost(id) {
  const response = await request(`/posts/${id}`);
  if (response.status === 404) return null;
  if (!response.ok) throw new Error(`get post failed: ${response.status}`);
  return response.json();
}

async function createPost({ title, body, userId = 1 }) {
  const response = await request("/posts", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title, body, userId }),
  });
  if (!response.ok) throw new Error(`create post failed: ${response.status}`);
  return response.json();
}

async function main() {
  console.log("-- list posts for user 1 --");
  for (const post of await listPosts({ userId: 1 })) {
    console.log(`  [${post.id}] ${post.title}`);
  }

  console.log("\n-- fetch post 1 --");
  const post = await getPost(1);
  console.log(`  title: ${post.title}`);

  console.log("\n-- fetch a post that does not exist --");
  console.log(`  result: ${await getPost(9999)}`);

  console.log("\n-- create a post --");
  const created = await createPost({ title: "Example title", body: "Example body." });
  console.log(`  server assigned id: ${created.id}`);
}

main().catch((error) => {
  console.error(`request failed: ${error.message}`);
  process.exit(1);
});
