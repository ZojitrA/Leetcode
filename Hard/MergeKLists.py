class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        if not len(lists):
            return None

        new_list = ListNode("end")
        saved = new_list
        last_thru = saved
        while len(lists):

            min = float("inf")
            idx = "no"
            pop = "no"

            for i, el in enumerate(lists):
                if el == None:
                    pop = i
                if el and el.val < min:
                    min = el.val
                    idx = i


            if idx != "no":
                lists[idx] = lists[idx].next
                new_list.val = min
                new_list.next = ListNode("end")
                new_list = new_list.next

            if pop != "no":
                lists.pop(pop)



        if last_thru.val == "end":
            last_thru.val = ""
            last_thru = None
        else:
            while last_thru.next and last_thru.next.val != "end":
                last_thru = last_thru.next

            last_thru.next = None
        return saved
                
