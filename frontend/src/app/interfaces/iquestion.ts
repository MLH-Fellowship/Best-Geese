export interface IQuestion {
    id?: string,
    tag: string,
    difficulty: string,
    question: string,
    options: string[],
    correct_answer: string
}
