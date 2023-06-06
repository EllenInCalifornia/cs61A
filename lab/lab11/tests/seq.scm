; helper function
; returns the values of lst that are bigger than x
; e.g., (larger-values 3 '(1 2 3 4 5 1 2 3 4 5)) --> (4 5 4 5)
(define (larger-values x lst)
  (filter (lambda (v) (> v x)) lst)
  )

(define (longest-increasing-subsequence lst)
  (if (null? lst)
    nil
    (begin
      (define first (car lst))
      (define rest (cdr lst))
      (define large-values-rest
        (larger-values first rest))
      (define with-first
        (list first (longest-increasing-subsequence rest))
      (define without-first
        (longest-increasing-subsequence rest))
        )
      (if (> (length with-first) (length without-first))
        with-first
        without-first))))