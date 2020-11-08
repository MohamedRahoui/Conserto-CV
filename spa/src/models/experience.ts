import base from '@models/base'

export default interface Experience extends base {
  title: string;
  employment_type: string;
  company: string;
  location: string;
  start_year: number;
  start_month: number;
  end_year: number;
  end_month: number;
  description: string;
}

export interface ExperienceState {
  experiences: Experience[],
  fetched: boolean
}

export const ExperienceURL = 'experiences/'
