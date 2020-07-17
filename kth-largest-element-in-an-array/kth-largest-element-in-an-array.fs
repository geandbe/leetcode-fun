let findKthLargest k nums =
    nums |> Seq.sort |> Seq.rev |> Seq.item (k - 1)

assert (findKthLargest 2 [3; 2; 1; 5; 6; 4] = 5)


