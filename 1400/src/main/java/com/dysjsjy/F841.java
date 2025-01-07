
// 错误写法
class F841 {
    int[] visited;

    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        visited = new int[rooms.size()];
        visit(rooms, rooms[0][0]);
        
        for (int i : visited) {
            if (i != 1) {
                return false;
            }
        }

        return true;
    }

    void visit(List<List<Integer>> rooms, List<Integer> keys) {
        if (keys == null) {
            return;
        }

        for (int i = 0; i < keys.size(); i++) {
            visited[keys[i]] = 1;
            visit(rooms, rooms[0][keys[i]]);
        }
    }
}