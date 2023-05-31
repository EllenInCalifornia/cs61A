(define (list-concat a b)
  (if (null? a) b
                (cons (car a) (list-concat (cdr a) b)))
  )

(define (remove item lst)
  (cond ((null? lst) '())
    ((equal? item (car lst)) (remove item (cdr lst)))
    (else (cons (car lst) (remove item (cdr lst))))
    )
  )

(define (remove_filter item lst)
  (filter (lambda (x) (not (= item x))) lst)
  )