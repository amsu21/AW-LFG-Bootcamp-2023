import { TrimTextPipe } from "./trimText.pipe";

fdescribe("Trim text pipe", () => {
    fit("shoudl trim the given text when esxceeded the given length", () => {
        const txt = 'Consequat id eu aute occaecat nostrud elit',
            maxLength = 10,
            expectedResult = 'Consequat';
        
            const sut = new TrimTextPipe();

            const actualResult = sut.transform(txt, maxLength);

            expect(actualResult).toBe(expectedResult)
    })
})