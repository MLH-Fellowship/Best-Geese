import { TestBed } from '@angular/core/testing';

import { QuestionProviderService } from './question-provider.service';

describe('QuestionProviderService', () => {
  let service: QuestionProviderService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(QuestionProviderService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
